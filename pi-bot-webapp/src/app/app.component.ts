import { CommandService } from './core/services/command.service';
import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent {

  responses: string[];

  constructor(private commandService: CommandService) {}

  sendEvent(eventName: string) {
    this.commandService.sendEvent(eventName).subscribe(
      response => {
        this.responses.push(response);
      }
    );
  }

}
