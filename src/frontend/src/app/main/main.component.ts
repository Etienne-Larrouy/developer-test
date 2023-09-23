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
    json_data: any = {};

    // Read content of json file
    onFileSelect(input: any) {
        console.log(input.files);
        if (input.files && input.files[0]) {
            var reader = new FileReader();
            reader.onload = (e: any) => {
                console.log('Got here: ', e.target.result);
                this.getOdds(e.target.result)
            }
            reader.readAsDataURL(input.files[0]);
        }
    }

    getOdds(json_data: any){
        this.service.getOddsFromfile(json_data).subscribe((data: Odds) => this.odds = data.odds);
    }
}


