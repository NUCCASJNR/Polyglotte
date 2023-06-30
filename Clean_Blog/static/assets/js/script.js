// "use strict";
//
// document.addEventListener("DOMContentLoaded", function () {
//     const updateBtn = document.getElementById('update');
//     const form = document.getElementById('update_form');
//     const modal = document.getElementById('modal-1')
//
//     updateBtn.addEventListener('click', function () {
//         const formData = new FormData(form);
//         console.log(formData)
//         fetch('/account', {method: 'POST', body: formData})
//             .then(function (response) {
//                 if (response.ok) {
//                     console.log('Form submitted successfully');
//                 } else {
//                     console.error('An Error occurred during form submission');
//                 }
//
//                 // const bootstrapModal = bootstrap.Modal.getInstance(modal);
//                 // bootstrapModal.hide();
//         });
//                 // .catch(function (error) {
//         //     console.log(error);
//         // });
//     });
//     modal.addEventListener('hidden.bs.modal', function () {
//         document.getElementById('update_form').reset();
//     });
// });
//
