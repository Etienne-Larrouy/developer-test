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

    odds: number = 63;

    getOdds(){
        this.service.getOddsFromfile().subscribe((data: Odds) => this.odds = data.odds);
    }
}


