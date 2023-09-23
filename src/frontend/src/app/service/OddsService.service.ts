import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { environment } from 'src/environments/environment';
import { Odds } from './odds';


@Injectable()
export class OddsService {
    baseUrl = environment.apiBaseUrl;
    constructor( private http: HttpClient) {}

     // Get odds from json file
     getOddsFromfile(json_data: any) {
        const formData = new FormData();
        formData.append("empire_plan.json", json_data, "empire_plan.json");
        return this.http.post<Odds>(this.baseUrl + '/odds', formData);
    }

}
