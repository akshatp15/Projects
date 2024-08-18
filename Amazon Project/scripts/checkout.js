import {renderOrderSummary} from './checkout/orderSummary.js';
import{renderPaymentSummary} from './checkout/paymentSummary.js';
import { loadProductsFetch, loadProducts } from '../data/products.js';
async function loadPage(){
  try{
    await loadProductsFetch();
  }
  catch(error){
    console.log('Unexpected error, please try again');
  }
  renderOrderSummary();
  renderPaymentSummary();
}
loadPage();