import { blankScreen } from './lib/blankScreen';
import { injectJsError } from './lib/jsError';
import { injectXHR } from './lib/xhr';
import { timing } from './lib/timing';
import { pv } from './lib/pv';


injectJsError();
injectXHR();
blankScreen();
timing();
pv();