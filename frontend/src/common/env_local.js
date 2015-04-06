import prod from "./env_prod";
import $ from 'jquery';

let env = $.extend(prod, {
  api_url : 'http://localhost:8080'
});

export default env
