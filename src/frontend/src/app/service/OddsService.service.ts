import { Injectable } from '@angular/core';
import { HttpClient, HttpErrorResponse } from '@angular/common/http';
import { environment } from 'src/environments/environment';
import { Odds } from './odds';
import { Observable, throwError } from 'rxjs';
import { catchError } from 'rxjs/operators';


@Injectable()
export class OddsService {
    baseUrl = environment.apiBaseUrl;
    constructor( private http: HttpClient) {}

     // Get odds from json file
    public getOddsFromfile(json_data: any): Observable<any>  {
        const formData = new FormData();
        formData.append("empire_plan.json", json_data, "empire_plan.json");
        return this.http.post<Odds>(this.baseUrl + '/odds', formData).pipe(
            catchError(this.handleError)
          );
    }

    private handleError(error: HttpErrorResponse): Observable<string> {
        let errorObj: any = {};
        if (error.error instanceof ErrorEvent) {
          // A client-side or network error occurred. Handle it accordingly.
          errorObj.statusText = error.error.message;
        } else {
          // The backend returned an unsuccessful response code.
          // The response body may contain clues as to what went wrong,
          errorObj.status = error.status;
          errorObj.statusText = error.statusText;
        }
        // return an observable with a user-facing error message
        return throwError(errorObj);
      }

}
