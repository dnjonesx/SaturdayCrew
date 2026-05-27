import type Weather from '@/Types/Weather';
import type WeatherHour from '@/Types/WeatherHour';
import type WeatherDay from '@/Types/WeatherDay';

const weatherTest = '{ "latitude": 52.52, "longitude": 13.419, "location": "NameOfPlace","timezone": "Europe/Berlin","timezone_abbreviation": "CEST","hourly": { "time": ["2022-07-01T00:00", "2022-07-01T01:00", "2022-07-01T02:00", "2022-07-01T03:00", "2022-07-01T04:00", "2022-07-01T05:00", "2022-07-01T06:00", "2022-07-01T07:00", "2022-07-01T08:00"], "temperature_2m": [13, 12.7, 12.7, 12.5, 12.5, 12.8, 13, 12.9, 13.3],  "wind": ["idk mate", "wimdy", "fuckin wimdy", "nothing", "stale", "tornado", "shelter indoors", "good luck", "enough for the wind chimes"], "precipitation": ["idk mate", "eh nothin", "fuckin rainy", "nothing", "dry", "thunder", "shelter indoors", "good luck", "enough for the umbrellas"]},"temp_units": { "temperature_2m": "°C"},"daily": { "day": ["2022-07-01", "2022-07-02", "2022-07-03", "2022-07-04", "2022-07-05", "2022-07-06", "2022-07-07", "2022-07-08", "2022-07-09" ], "max_temperature": [13, 12.7, 12.7, 12.5, 12.5, 12.8, 13, 12.9, 13.3], "min_temperature": [1, 1.7, 1.7, 1.5, 1.5, 1.8, 1, 2.9, 3.3] }}';

// {
//     "latitude": 52.52,
//     "longitude": 13.419,
//     "location": "NameOfPlace",
//     "timezone": "Europe/Berlin",
//     "timezone_abbreviation": "CEST",
//     "hourly": {
//         "time": ["2022-07-01T00:00", "2022-07-01T01:00", "2022-07-01T02:00", "2022-07-01T03:00", "2022-07-01T04:00", "2022-07-01T05:00", "2022-07-01T06:00", "2022-07-01T07:00", "2022-07-01T08:00"],
//         "temperature_2m": [13, 12.7, 12.7, 12.5, 12.5, 12.8, 13, 12.9, 13.3], 
//         "wind": ["idk mate", "wimdy", "fuckin wimdy", "nothing", "stale", "tornado", "shelter indoors", "good luck", "enough for the wind chimes"],
//         "precipitation": ["idk mate", "eh nothin", "fuckin rainy", "nothing", "dry", "thunder", "shelter indoors", "good luck", "enough for the umbrellas"]
//     },
//     "temp_units": {
//         "temperature_2m": "°C"
//     },
//     "daily": {
//         "day": ["2022-07-01", "2022-07-02", "2022-07-03", "2022-07-04", "2022-07-05", "2022-07-06", "2022-07-07", "2022-07-08", "2022-07-09" ],
//         "max_temperature": [13, 12.7, 12.7, 12.5, 12.5, 12.8, 13, 12.9, 13.3],
//         "min_temperature": [1, 1.7, 1.7, 1.5, 1.5, 1.8, 1, 2.9, 3.3]
//     }
// }

export default {
    fromWeatherToHourlyWeather(weather: Weather): Array<WeatherHour> {
        // has lots of information, needs to return an array of weather hours
        let list = new Array() as Array<WeatherHour>;

        // console.log(weather);
        if (weather == null) return list;

        for (let i = 0; i<weather.hourly.time.length; i++) {
            list.push({
                time: weather.hourly.time[i], 
                temp: weather.hourly.temperature_2m[i], 
                precip: weather.hourly.precipitation[i], 
                wind: weather.hourly.wind[i]
            } as WeatherHour);
        }
        
        return list;
    },

    // hourly: {
    //     time: String[];
    //     temperature_2m: number[];
    //     wind: String[];
    //     precipitation: String[];
    // }

    // id: null;
    // time: String;
    // temp: number;
    // precip: String;
    // wind: String;

    fromWeatherToDailyWeather(weather: Weather): Array<WeatherDay> {
        // has lots of information, needs to return an array of weather days
        let list = new Array() as Array<WeatherDay>;

        // weather = JSON.parse(weatherTest);

        // console.log(weather);
        if (weather == null) return list;
        
        for (let i = 0; i<weather.daily.day.length; i++) {
            list.push({
                day: weather.daily.day[i],
                minTemp: weather.daily.min_temperature[i], 
                maxTemp: weather.daily.max_temperature[i]
            } as WeatherDay);
        }

        return list;
    }, 

    // daily: {
    //     day: String[];
    //     max_temperature: number[];
    //     min_temperature: number[];
    // }

    // id: null;
    // day: String;
    // minTemp: number;
    // maxTemp: number;

    getWeatherFromCoors(latitute: String, longitude: String) {

    }, 

    getWeatherFromLocation(location: String) {

    }, 

    getWeatherRandom() {
        
    }, 

    getWeatherHourlyTest(): Array<WeatherHour> {
        // has lots of information, needs to return an array of weather hours
        let list = new Array() as Array<WeatherHour>;

        // let weather = JSON.parse(JSON.stringify(weatherFile));
        let weather = JSON.parse(weatherTest);

        console.log(weather);
        if (weather == null) return list;

        for (let i = 0; i<weather.hourly.time.length; i++) {
            console.log(weather);
            console.log("weather ^");
            list.push({
                time: weather.hourly.time[i], 
                temp: weather.hourly.temperature_2m[i], 
                precip: weather.hourly.precipitation[i], 
                wind: weather.hourly.wind[i]
            } as WeatherHour);
        }
        
        return list;
    },

    getWeatherDailyTest(): Array<WeatherDay> {
        // has lots of information, needs to return an array of weather hours
        let list = new Array() as Array<WeatherDay>;

        // let weather = JSON.parse(JSON.stringify(weatherFile));
        let weather = JSON.parse(weatherTest);

        console.log(weather);
        if (weather == null) return list;

        for (let i = 0; i<weather.daily.day.length; i++) {
            list.push({
                day: weather.daily.day[i],
                minTemp: weather.daily.min_temperature[i], 
                maxTemp: weather.daily.max_temperature[i]
            } as WeatherDay);
        }
        
        return list;
    }, 

    getWeatherTest() {
        return JSON.parse(weatherTest);
    }
}



