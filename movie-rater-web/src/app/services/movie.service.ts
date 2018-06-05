import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { environment } from '../../environments/environment';
import { HttpHeaders, HttpClient } from '@angular/common/http';

@Injectable()
export class MovieService {

  httpHeaders = new HttpHeaders({'Content-Type':'application/json; charset=utf-8'});
  baseUrl: string = environment.apiUrl;

  constructor(private http: HttpClient) { }

  getMovies(): Observable<any>{
    return this.http.get(this.baseUrl + 'movies/', this.getAuthHeaders());
  }

private getAuthHeaders(){
  const token = localStorage.getItem('token');
  const httpHeaders = new HttpHeaders(
    {'Content-Type': 'application/json; charset=utf-8',
  'Authorization': 'Token' + token});
  return {headers: httpHeaders};
}
}

