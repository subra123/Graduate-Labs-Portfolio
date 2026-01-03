fn average_temperature(temps: &[f64]) -> f64 {
    let sum: f64 = temps.iter().sum();
    sum / temps.len() as f64
}

fn main() {
    let weekly_temps = [25.6, 27.3, 26.1, 28.9, 30.2, 29.8, 31.0];
    
    let last_three_days = &weekly_temps[4..];
    
    let avg_temp = average_temperature(last_three_days);
    println!("Average temperature for the last 3 days: {:.2}°C", avg_temp);
}
