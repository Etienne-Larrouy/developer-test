import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { environment } from 'src/environments/environment';
import { Odds } from './odds';


@Injectable()
export class OddsService {
    baseUrl = environment.apiBaseUrl;
    constructor( private http: HttpClient) {}

     // Get odds from json file
     getOddsFromfile() {
        return this.http.get<Odds>(this.baseUrl + '/odds');
    }

}
