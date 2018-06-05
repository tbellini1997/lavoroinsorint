import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable } from 'rxjs';
import { environment } from '../../environments/environment.prod';

@Injectable()
export class UserService {

  httpHeaders = new HttpHeaders({'Content-Type':'application/json; charset=utf-8'});
  baseUrl: string = environment.apiUrl;

  constructor(private http: HttpClient) { }

  loginUser(userData: any): Observable<any>{
    return this.http.post(this.baseUrl + 'auth/', userData,{headers: this.httpHeaders} );
  }
}
