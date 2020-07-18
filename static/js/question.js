document.addEventListener('DOMContentLoaded', () => {
    document.querySelector('#show-question-form').addEventListener('click', event => {
      event.preventDefault()
      document.querySelector('#question-form').classList.remove('dn')
      document.querySelector('#id_amount').focus()
    })
  })