# GPS model for trajectory simulation

#def add_gps_noise(df, noise_std, bias_drift_std = 0.0) -> pd.DataFrame
    # takes trajectory df, returns a copy with gps_x, gps_y columns added
    # (keep truth columns intact - never overwrite x, y)