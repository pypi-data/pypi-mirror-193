# -*- coding: utf-8 -*-
import numpy as np
import timesynth as ts
import random
from tqdm import tqdm
from sklearn.preprocessing import minmax_scale

class RandomTS:
    def __init__(self,
                 min_samples,
                 max_samples,
                 frequency=None,
                 intermittent_pct=.05):
        self.num_points = random.randint(min_samples, max_samples)
        if frequency is None:
            frequency = random.randint(2, max_samples)
        self.frequency = frequency
        self.intermittent_pct = intermittent_pct
        return

    def add_outliers(self, series):
        n = len(series)
        outlier_perc = random.random()
        num_outliers = random.randint(1,
                                      max(int(.2 * n), int(outlier_perc*n)))
        outlier_index = [np.random.choice(range(n)) for i in range(num_outliers)]
        series[outlier_index] = series[outlier_index] + (random.randint(-1, 1) * random.random()) * series[outlier_index]
        return minmax_scale(series)

    def generate_sinusoidal(self):
        time_sampler = ts.TimeSampler()
        irregular_time_samples = time_sampler.sample_irregular_time(num_points=self.num_points)
        std = random.random()
        sinusoid = ts.signals.Sinusoidal(frequency=self.frequency)
        white_noise = ts.noise.GaussianNoise(std=std)
        timeseries = ts.TimeSeries(sinusoid, noise_generator=white_noise)
        samples, signals, errors = timeseries.sample(irregular_time_samples)
        if random.random() > .5:
            trend = random.uniform(-.01, .01)
            samples = samples + trend*np.array(range(self.num_points))
        return minmax_scale(samples.reshape(-1, 1))

    def generate_psuedoperiodic(self):
        time_sampler = ts.TimeSampler()
        irregular_time_samples = time_sampler.sample_irregular_time(num_points=self.num_points)
        frequency = self.frequency*2
        freqSD = random.uniform(.005, .1)
        pseudo_periodic = ts.signals.PseudoPeriodic(frequency=frequency,
                                                    freqSD=freqSD,
                                                    ampSD=0.5)
        timeseries_pp = ts.TimeSeries(pseudo_periodic)
        samples, signals, errors = timeseries_pp.sample(irregular_time_samples)
        if random.random() > .5:
            trend = random.uniform(-.01, .01)
            samples = samples + trend*np.array(range(self.num_points))
        return minmax_scale(samples.reshape(-1, 1))
    
    def generate_car(self):
        time_sampler = ts.TimeSampler()
        irregular_time_samples = time_sampler.sample_irregular_time(num_points=self.num_points)
        ar_param = random.uniform(0, 1)
        sigma = random.uniform(0.01, .11)
        car = ts.signals.CAR(ar_param=ar_param, sigma=sigma)
        car_series = ts.TimeSeries(signal_generator=car)
        samples = car_series.sample(irregular_time_samples)[0]
        return minmax_scale(samples.reshape(-1, 1))

    def generate_mean_noise(self):
        sigma = 1 * np.sqrt(random.randint(100, 3000/2))
        samples = np.random.normal(random.randint(1,3000), sigma, self.num_points)
        return minmax_scale(samples.reshape(-1, 1))
    
    def generate_local_constant(self):
        sigma = 1 * np.sqrt(random.randint(100, 3000/2))
        samples = np.random.normal(random.randint(1,3000), sigma, self.num_points)
        samples[:int(self.num_points/2)] = samples[:int(self.num_points/2)] + np.random.normal(random.randint(1,3000))
        return minmax_scale(samples.reshape(-1, 1))
    
    def generate_simple_trend(self):
        error = True
        while error:
            try:
                initial = random.randint(1,10000)
                end = random.randint(1,10000)
                if end < initial:
                    simple_trend = np.arange(end, initial, step=random.randint(1, 10))[:self.num_points]
                else:
                    simple_trend = np.arange(initial, end, step=random.randint(1, 10))[:self.num_points]
                sigma = 1 * np.sqrt(random.randint(100, 3000/2))
                noise = np.random.normal(random.randint(0,100), sigma, self.num_points)
                if random.random() < .8:
                    simple_trend = simple_trend + noise
                error = False
            except:
                pass
        return minmax_scale(simple_trend.reshape(-1, 1))

    def generate_outlier_trend(self):
        error = True
        while error:
            try:
                initial = random.randint(1,10000)
                end = random.randint(1,10000)
                if end < initial:
                    simple_trend = np.arange(end, initial, step=random.randint(1, 500))[:self.num_points]
                else:
                    simple_trend = np.arange(initial, end, step=random.randint(1, 500))[:self.num_points]
                if random.random() < .8:
                    simple_trend = simple_trend

                simple_trend[5] = simple_trend[5] + simple_trend[5]*.2
                simple_trend[12] = simple_trend[12] + simple_trend[12]*.2
                error = False
            except:
                pass
        return minmax_scale(simple_trend.reshape(-1, 1))

    def generate_local_trend(self):
        error = True
        while error:
            try:
                initial = random.randint(1,10000)
                end = random.randint(1,10000)
                if end < initial:
                    simple_trend = np.arange(end, initial, step=random.randint(1, 10))[:int(self.num_points/2)]
                else:
                    simple_trend = np.arange(initial, end, step=random.randint(1, 10))[:int(self.num_points/2)]
                initial = simple_trend[-1]
                sigma = 1 * np.sqrt(random.randint(100, 3000/2))
                noise = np.random.normal(random.randint(0,100), sigma, int(self.num_points/2))
                simple_trend = simple_trend + noise
                simple_trend_2 = -simple_trend - (-simple_trend[-1] - initial)
                local_trend = np.append(simple_trend, simple_trend_2)
                error = False
            except Exception as e:
                pass
        return minmax_scale(local_trend.reshape(-1, 1))

    def generate_simple_seasonal(self):
        duration = self.num_points
        periodicity = self.frequency
        harmonics = 3
        noise_std = random.randint(10,2000)
        total_cycles = duration / periodicity
        duration = periodicity * total_cycles
        # assert duration == int(duration)
        duration = int(duration)
        harmonics = harmonics if harmonics else int(np.floor(periodicity / 2))
    
        lambda_p = 2 * np.pi / float(periodicity)
    
        gamma_jt = noise_std * np.random.randn((harmonics))
        gamma_star_jt = noise_std * np.random.randn((harmonics))
    
        total_timesteps = 100 * duration # Pad for burn in
        series = np.zeros(total_timesteps)
        for t in range(total_timesteps):
            gamma_jtp1 = np.zeros_like(gamma_jt)
            gamma_star_jtp1 = np.zeros_like(gamma_star_jt)
            for j in range(1, harmonics + 1):
                cos_j = np.cos(lambda_p * j)
                sin_j = np.sin(lambda_p * j)
                gamma_jtp1[j - 1] = (gamma_jt[j - 1] * cos_j
                                     + gamma_star_jt[j - 1] * sin_j
                                     + noise_std * np.random.randn())
                gamma_star_jtp1[j - 1] = (- gamma_jt[j - 1] * sin_j
                                          + gamma_star_jt[j - 1] * cos_j
                                          + noise_std * np.random.randn())
            series[t] = np.sum(gamma_jtp1)
            gamma_jt = gamma_jtp1
            gamma_star_jt = gamma_star_jtp1
        wanted_series = series[-duration:] # Discard burn in
        samples = (wanted_series - min(wanted_series) + 10000)/1000
        return minmax_scale(samples.reshape(-1, 1))

    def generate_trend_seasonal(self):
        seasonal = self.generate_simple_seasonal()
        trend = self.generate_simple_trend()
        length = min(len(seasonal), len(trend))
        samples = seasonal[:length] + trend[:length]
        return minmax_scale(samples.reshape(-1, 1))

    def generate(self):
        self.model = random.choice([
                                'simple_seasonal', 
                                'simple_seasonal', 
                                'sinusoidal', 
                                'psuedoperiodic', 
                                'car', 
                                'car', 
                                'mean_noise', 
                                'mean_noise',
                                'simple_trend',
                                'trend_seasonal',
                                'local_trend',
                                'local_constant',
                                # 'outlier_trend',
                               ])
        mapping = {'sinusoidal': self.generate_sinusoidal,
                   'psuedoperiodic': self.generate_psuedoperiodic,
                   'car': self.generate_car,
                   'mean_noise': self.generate_mean_noise,
                   'simple_seasonal': self.generate_simple_seasonal,
                   'simple_trend': self.generate_simple_trend,
                   'local_trend': self.generate_local_trend,
                   'trend_seasonal': self.generate_trend_seasonal,
                   'local_constant': self.generate_local_constant,
                   'outlier_trend': self.generate_outlier_trend
                   }
        func = mapping[self.model]
        samples = func()
        samples = self.add_outliers(samples)
        return samples #* random.randint(1, 1000)

#%%

if __name__ == '__main__':
    import matplotlib.pyplot as plt
    from TSUtilities.get_features import FeatureExtraction
    for i in tqdm(range(20)):
        generator = RandomTS(50, 100, frequency=12)
        series = generator.generate()
        freq = generator.frequency
        plt.plot(series)
        plt.show()
        extractor = FeatureExtraction(series, freq)
        features = extractor.extract()
        look = extractor.diff_series
