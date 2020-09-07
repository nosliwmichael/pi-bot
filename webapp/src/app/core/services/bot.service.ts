import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { HttpClient } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class BotService {

  private readonly CONTROL_ENDPOINT = '/control';
  private readonly STREAM_ENDPOINT = '/stream';

  constructor(private http: HttpClient) { }

  getStreamUrl(): string {
    return `${this.STREAM_ENDPOINT}`;
  }

  sendEvent(eventName: string): Observable<{message: string}> {
    return this.http.post<{message: string}>(`${this.CONTROL_ENDPOINT}`, { event: eventName });
  }

}
