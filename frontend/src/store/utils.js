export function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}


export class Storage {

    get(key) {
        let get_value;
        try {
            var storage_value = localStorage.getItem(key)
            get_value = storage_value
        } catch {
            get_value = null
        }

        return get_value
    }

    set(key, value) {
        localStorage.setItem(key, value)
    }

    remove(key) {
        localStorage.removeItem(key)
    }
}
