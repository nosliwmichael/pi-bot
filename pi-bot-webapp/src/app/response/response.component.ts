import { Component, OnInit, ViewChild, ElementRef, AfterViewChecked, Input } from '@angular/core';

@Component({
  selector: 'app-response',
  templateUrl: './response.component.html',
  styleUrls: ['./response.component.scss']
})
export class ResponseComponent implements OnInit, AfterViewChecked {

  @Input() responses: string[];

  @ViewChild('console', { static: false }) private console: ElementRef;

  constructor() {}

  ngOnInit() {
  }

  ngAfterViewChecked() {
    this.scrollToBottom();
  }

  scrollToBottom(): void {
    try {
      this.console.nativeElement.scrollTop = this.console.nativeElement.scrollHeight;
    } catch (err) { console.error(err); }
  }

}
