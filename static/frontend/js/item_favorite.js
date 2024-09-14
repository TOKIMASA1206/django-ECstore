document.addEventListener('DOMContentLoaded', function() {
  document.querySelectorAll('.favorite-btn').forEach(function(button) {
      button.addEventListener('click', function() {
          const itemId = button.getAttribute('data-item-id');

          if (!itemId) {
              console.error('Item ID is missing');
              return;
          }

          fetch(`/item/${itemId}/toggle_favorite/`, {
              method: 'POST',
              headers: {
                  'Content-Type': 'application/x-www-form-urlencoded',
                  'X-CSRFToken': getCsrfToken()
              },
              body: new URLSearchParams({
                  'item_id': itemId  // POSTデータのキー名をitem_idに変更
              })
          })
          .then(response => response.json())
          .then(data => {
              if (data.is_favorite) {
                  button.innerHTML = '<i class="fa-solid fa-heart text-danger"></i>';
              } else {
                  button.innerHTML = '<i class="fa-regular fa-heart text-danger"></i>';
              }
          })
          .catch(error => console.error('Error:', error));
      });
  });
});

function getCsrfToken() {
  let csrfToken = null;
  const cookies = document.cookie.split(';');
  for (let cookie of cookies) {
      cookie = cookie.trim();
      if (cookie.startsWith('csrftoken=')) {
          csrfToken = cookie.substring('csrftoken='.length, cookie.length);
          break;
      }
  }
  return csrfToken;
}

