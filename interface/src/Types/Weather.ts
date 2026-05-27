export default interface Weather {
    id: null;
    latitude: number;
    longitude: number;
    location: String;
    timezone: String;
    timezone_abbreviation: String;
    hourly: {
        time: String[];
        temperature_2m: number[];
        wind: String[];
        precipitation: String[];
    }
    temp_units: String;
    daily: {
        day: String[];
        max_temperature: number[];
        min_temperature: number[];
    }
    // current_weather: String;
}