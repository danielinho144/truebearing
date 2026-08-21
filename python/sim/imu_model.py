# IMU model for trajectory simulation

#def add_imu_noise(df, accel_noise_std, gyro_noise_std) -> pd.DataFrame
    # for now: accel/gyro are ~zero (straight line, const velocity)
    # adds imu_ac, imu_ay, imu_gyro columns
    # note: revisit once a turning/accelerating profile exists
