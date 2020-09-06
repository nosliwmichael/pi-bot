import { BrowserModule } from '@angular/platform-browser';
import { SharedModule } from './shared/shared.module';
import { NgModule } from '@angular/core';

import { AppComponent } from './app.component';
import { ResponseComponent } from './response/response.component';
import { CoreModule } from './core/core.module';
import { ControlPadComponent } from './control-pad/control-pad.component';
import { FaIconComponent } from '@fortawesome/angular-fontawesome';

@NgModule({
  declarations: [
    AppComponent,
    ResponseComponent,
    ControlPadComponent,
  ],
  imports: [
    CoreModule,
    SharedModule,
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule {}
