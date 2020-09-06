import { BotService } from './core/services/bot.service';
import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent implements OnInit {

  responses: string[] = [];

  constructor(private botService: BotService) {}

  ngOnInit(): void {
    this.stream();
  }

  sendEvent(eventName: string) {
    this.botService.sendEvent(eventName).subscribe(
      response => {
        this.responses.push(response.message);
      },
    );
  }

  stream() {
    this.botService.stream().subscribe(
      response => {
        console.log(response);
      }
    );
  }

}
