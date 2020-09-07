import { BotService } from './core/services/bot.service';
import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent implements OnInit {

  showConsole = false;
  showControls = true;
  responses: string[] = [];
  streamUrl: string;

  constructor(private botService: BotService) {}

  ngOnInit(): void {
    this.streamUrl = this.botService.getStreamUrl();
  }

  sendEvent(eventName: string) {
    this.botService.sendEvent(eventName).subscribe(
      response => {
        this.responses.push(response.message);
      },
    );
  }

}
