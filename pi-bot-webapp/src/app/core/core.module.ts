import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { HttpClientModule } from '@angular/common/http';
import { FontAwesomeModule } from '@fortawesome/angular-fontawesome';

@NgModule({
  declarations: [],
  imports: [
    HttpClientModule,
  ],
  exports: [
    BrowserModule,
    FontAwesomeModule,
  ]
})
export class CoreModule { }
