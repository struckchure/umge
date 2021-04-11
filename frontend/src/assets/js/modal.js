export function show_modal(modal_id) {
  var modal = document.getElementById(modal_id)
  modal.style.display = 'block'
}

export function close_modal(modal_id) {
  var modal = document.getElementById(modal_id)
  modal.style.display = 'none'
}
