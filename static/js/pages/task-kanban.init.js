dragula([document.getElementById("upcoming-task"), document.getElementById("inprogress-task"), document.getElementById("test-task"), document.getElementById("complete-task")])
    .on('drag', function(el, container) {
        if (container.id === 'upcoming-task') {
            el.className = el.className.replace(' task_status_1', '');
        }
        if (container.id === 'inprogress-task') {
            el.className = el.className.replace(' task_status_2', '');
        }
        if (container.id === 'test-task') {
            el.className = el.className.replace(' task_status_3', '');
        }
        if (container.id === 'complete-task') {
            el.className = el.className.replace(' task_status_4', '');
        }
    })
    .on("drop", function(el, container) {
        function getCookie(name) {
            let cookieValue = null;
            if (document.cookie && document.cookie !== '') {
                const cookies = document.cookie.split(';');
                for (let i = 0; i < cookies.length; i++) {
                    const cookie = cookies[i].trim();
                    if (cookie.substring(0, name.length + 1) === (name + '=')) {
                        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                        break;
                    }
                }
            }
            return cookieValue;
        }
        const csrftoken = getCookie('csrftoken');


        function send_data_1(id) {
            $.ajax({
                url: '/tasks/kanbanboard',
                type: 'POST',
                data: {
                    status: 1,
                    task_id: id
                },
                beforeSend: function(xhr) {
                    xhr.setRequestHeader("X-CSRFToken", csrftoken);
                },
                error: function(resp) {
                    console.log("Something went wrong");
                },
            });
        }


        function send_data_2(id) {
            $.ajax({
                url: '/tasks/kanbanboard',
                type: 'POST',
                data: {
                    status: 2,
                    task_id: id
                },
                beforeSend: function(xhr) {
                    xhr.setRequestHeader("X-CSRFToken", csrftoken);
                },
                error: function(resp) {
                    console.log("Something went wrong");
                }
            });
            window.location.reload();
        }
        setTimeout('send_data_2(id)', 200);

        function send_data_3(id) {
            $.ajax({
                url: '/tasks/kanbanboard',
                type: 'POST',
                data: {
                    status: 3,
                    task_id: id
                },
                beforeSend: function(xhr) {
                    xhr.setRequestHeader("X-CSRFToken", csrftoken);
                },
                error: function(resp) {
                    console.log("Something went wrong");
                }
            });
            window.location.reload();

        }
        setTimeout('send_data_3(id)', 200);

        function send_data_4(id) {
            $.ajax({
                url: '/tasks/kanbanboard',
                type: 'POST',
                data: {
                    status: 4,
                    task_id: id
                },
                beforeSend: function(xhr) {
                    xhr.setRequestHeader("X-CSRFToken", csrftoken);
                },
                error: function(resp) {
                    console.log("Something went wrong");
                }
            });
            window.location.reload();

        }
        setTimeout('send_data_4(id)', 200);

        if (container.id === 'upcoming-task') {
            el.className += ' task_status_1';
            send_data_1(el.id);
        }
        if (container.id === 'inprogress-task') {
            el.className += ' task_status_2';
            send_data_2(el.id);
        }
        if (container.id === 'test-task') {
            el.className += ' task_status_3';
            send_data_3(el.id);
        }
        if (container.id === 'complete-task') {
            el.className += ' task_status_4';
            send_data_4(el.id);
        }
    });