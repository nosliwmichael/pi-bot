import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { HttpClient } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class BotService {

  private readonly IS_LOCAL = true;
  private readonly DOMAIN = this.IS_LOCAL ? 'http://localhost' : 'http://192.168.1.219';
  private readonly PORT = ':5000';
  private readonly BASE_URL = `${this.DOMAIN}${this.PORT}`;
  private readonly CONTROL_ENDPOINT = '/control';
  private readonly STREAM_ENDPOINT = '/stream';

  constructor(private http: HttpClient) { }

  stream(): Observable<any> {
    return this.http.get<any>(`${this.BASE_URL}${this.STREAM_ENDPOINT}`);
  }

  sendEvent(eventName: string): Observable<{message: string}> {
    return this.http.post<{message: string}>(`${this.BASE_URL}${this.CONTROL_ENDPOINT}`, { event: eventName });
  }

}
