from bayes_opt import BayesianOptimization, UtilityFunction
from matplotlib import cm, pyplot as plt
import numpy as np
import pandas as pd


class DPBayesOpt:
    """A class to perform Bayesian Optimization with Differential Privacy to infer the surface azimuth and tilts of a solar PV system.

    Args:
        epsilon (float, optional): The DP epsilon parameter. Defaults to 1.
        delta (float, optional): The DP delta parameter. Defaults to 0.1.
        iterations (int, optional): The number of optimization iterations to run. Defaults to 100.
        f (callable, optional): The objective function. Defaults to None.
        verbose (int, optional): The verbosity of the optimizer. Choose 0 to silence the outputs. Choose 1 to print only when a maximum is observed. Choose 2 to print the output at each iteration. Defaults to 2.
        random_state (int, optional): The random seed of the optimizer. Defaults to 1.
    """

    def __init__(
        self,
        epsilon: float = 1,
        delta: float = 0.1,
        iterations: int = 100,
        f: callable = None,  # type: ignore
        pbounds: dict = {"surface_azimuth": (0, 360), "surface_tilt": (0, 90)},
        verbose: int = 2,
        random_state: int = 1,
        **BayesianOptimizerKwargs,
    ):
        self.epsilon = epsilon
        self.delta = delta
        self.iterations = iterations
        self.black_box_function = f
        self.verbose = verbose
        self.random_state = random_state
        self.optimizer = BayesianOptimization(
            f=f,
            pbounds=pbounds,
            verbose=self.verbose,  # verbose = 1 prints only when a maximum is observed, verbose = 0 is silent
            random_state=self.random_state,
            **BayesianOptimizerKwargs,
        )

        all_azimuth = np.arange(0, 360, 1)
        all_tilt = np.arange(0, 91, 1)
        self.all_pairs = np.stack(
            np.meshgrid(*[all_azimuth, all_tilt]), axis=-1
        ).reshape(-1, 2)
        self.num_of_pairs = len(self.all_pairs)
        self._c = 2 * np.sqrt(np.log(6 * self.num_of_pairs / self.delta))

    def optimize(self, **HotStartKwargs) -> None:
        """This method performs the Bayesian Optimization with Differential Privacy for the given number of iterations.

        Args:
            HotStartKwargs (dict): The keyword arguments to pass to the optimizer's maximize method.
        """
        self.optimizer.maximize(**HotStartKwargs)
        for t in range(self.iterations):
            self.phi = 2 * np.log(
                self.num_of_pairs * (t + 1) ** 2 * np.pi**2 / 3 / self.delta
            )
            utility = UtilityFunction(kind="ucb", kappa=self.phi)
            next_point = self.optimizer.suggest(utility)
            target = self.black_box_function(**next_point)
            self.optimizer.register(params=next_point, target=target)
            # if self.verbose:
            #     print(target, next_point)
        self.thetas = pd.DataFrame(
            pd.DataFrame(self.optimizer.res).params.tolist()
        ).values
        if self.verbose:
            print(self.optimizer.max)

    def plot(self) -> None:
        """This method plots the loglikelihoods of the surface azimuth and tilt pairs and the number of times each pair was sampled by the optimizer."""
        self.phi = 2 * np.log(
            self.num_of_pairs * (self.iterations + 1) ** 2 * np.pi**2 / 3 / self.delta
        )
        model_mean, model_std = self.optimizer._gp.predict(
            self.all_pairs, return_std=True
        )
        likelihoods = np.exp(
            self.epsilon * model_mean / 2 / (2 * np.sqrt(self.phi) + self._c)
        )
        likelihoods /= np.sum(likelihoods)
        theta0 = np.linspace(0, 359, 360)
        theta1 = np.linspace(0, 90, 91)
        Theta0, Theta1 = np.meshgrid(theta0, theta1)
        loglikelihoods = np.log(likelihoods)
        LLM = loglikelihoods.reshape(Theta0.shape)
        plt.pcolor(
            Theta0,
            Theta1,
            LLM,
            cmap=cm.RdYlBu,  # type: ignore
            alpha=0.75,
        )
        plt.colorbar(label="Loglikelihood")
        plt.hexbin(
            self.thetas[:, 0],
            self.thetas[:, 1],
            gridsize=(15, 10),  # type: ignore
            alpha=0.3,
            cmap=cm.get_cmap("PiYG", 11),
        )
        plt.colorbar(label="# Times sampled")
        plt.xlabel("Azimuth (degree)")
        plt.ylabel("Tilt (degree)")

    def infer(self, n=1, infer_epsilon=None) -> pd.Series:
        """This method returns the inferred surface azimuth and tilt pairs.

        Args:
            n (int, optional): The number of DP samples to draw. Defaults to 1.
            infer_epsilon (float, optional): The epsilon value to use for inference. This needs to be adjusted if we querying for more than one sample. Defaults to None.

        Returns:
            pd.Series: The inferred DP surface azimuth and tilt pairs.
        """
        if infer_epsilon is None:
            infer_epsilon = self.epsilon

        self.phi = 2 * np.log(
            self.num_of_pairs * (self.iterations + 1) ** 2 * np.pi**2 / 3 / self.delta
        )
        model_mean, _ = self.optimizer._gp.predict(self.thetas, return_std=True)
        likelihoods = np.exp(
            infer_epsilon * model_mean / 2 / (2 * np.sqrt(self.phi) + self._c)
        )
        likelihoods /= np.sum(likelihoods)
        loglikelihoods = np.log(likelihoods)
        results = (
            pd.DataFrame(
                np.hstack((self.thetas, likelihoods.reshape(-1, 1))),
                columns=["Az", "Tl", "LLM"],
            )
            .groupby(["Az", "Tl"], as_index=False)
            .first()
            .sample(n, weights="LLM", replace=True)
        )
        return results.mean()

    def to_json(self) -> dict:
        """A method to serialize the class.

        Returns:
            dict: A dictionary containing the class attributes.
        """
        return {
            "num_of_pairs": self.num_of_pairs,
            "iterations": self.iterations,
            "delta": self.delta,
            "epsilon": self.epsilon,
            "optimizer_gp": self.optimizer._gp,
            "c": self._c,
            "thetas": self.thetas,
            "max": self.optimizer.max,
        }
