import { Component } from '@angular/core';
import { Odds } from '../service/odds';
import { OddsService } from '../service/OddsService.service';

@Component({
    selector: 'app-main',
    templateUrl: './main.component.html',
    styleUrls: ['./main.component.scss']
})

export class MainComponent {

    constructor(private service: OddsService) {}

    odds: number = -1;
    json_data: any = {};

    // Read content of json file
    onFileSelect(input: any) {
        if (input.files && input.files[0]) {
            this.getOdds(input.files[0]);
        }
    }

    // Reach server to get odds from json file
    getOdds(json_data: any){
        this.service.getOddsFromfile(json_data).subscribe((data: Odds) => {
            this.odds = data.odds
        }, error => {
            console.log(error)
        });
    }
}


