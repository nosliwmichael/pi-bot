import { CommandService } from './../core/services/command.service';
import { Component, OnInit, Output, EventEmitter } from '@angular/core';
import { faCaretUp, faCaretLeft, faCaretRight, faCaretDown } from '@fortawesome/free-solid-svg-icons';
import { faStopCircle } from '@fortawesome/free-regular-svg-icons';

@Component({
  selector: 'app-control-pad',
  templateUrl: './control-pad.component.html',
  styleUrls: ['./control-pad.component.scss']
})
export class ControlPadComponent implements OnInit {

  @Output() controlEvent = new EventEmitter<string>();

  upIcon = faCaretUp;
  leftIcon = faCaretLeft;
  rightIcon = faCaretRight;
  downIcon = faCaretDown;
  stopIcon = faStopCircle;

  constructor() {}

  ngOnInit() {
  }

}
