import { BotService } from '../core/services/bot.service';
import { Component, OnInit, Output, EventEmitter, HostListener } from '@angular/core';
import { faCaretUp, faCaretLeft, faCaretRight, faCaretDown } from '@fortawesome/free-solid-svg-icons';
import { faStopCircle } from '@fortawesome/free-regular-svg-icons';

@Component({
  selector: 'app-control-pad',
  templateUrl: './control-pad.component.html',
  styleUrls: ['./control-pad.component.scss']
})
export class ControlPadComponent implements OnInit {

  @Output() controlEvent = new EventEmitter<string>();

  KEY_CODE = {
    ArrowUp: 'up_event',
    ArrowLeft: 'left_event',
    ArrowRight: 'right_event',
    ArrowDown: 'down_event',
    Escape: 'close_event',
  };

  upIcon = faCaretUp;
  leftIcon = faCaretLeft;
  rightIcon = faCaretRight;
  downIcon = faCaretDown;
  stopIcon = faStopCircle;

  constructor() {}

  ngOnInit() {
  }

  @HostListener('window:keyup', ['$event'])
  @HostListener('window:keydown', ['$event'])
  keyUpEvent(event: KeyboardEvent) {
    const motorEvent = this.KEY_CODE[event.key];
    if (motorEvent && event.type === 'keydown') {
      this.controlEvent.emit(motorEvent);
    } else if (motorEvent && event.type === 'keyup') {
      this.controlEvent.emit('stop_event');
    }
  }

}
