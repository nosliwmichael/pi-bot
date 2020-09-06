import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { HttpClient } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class CommandService {

  private readonly DOMAIN = 'http://192.168.1.219';
  private readonly PORT = ':5000';
  private readonly ENDPOINT = '/pi-bot';
  private readonly BASE_URL = `${this.DOMAIN}${this.PORT}${this.ENDPOINT}`;

  constructor(private http: HttpClient) { }

  sendEvent(eventName: string): Observable<string> {
    return this.http.post<string>(this.BASE_URL, { event: eventName });
  }

}
