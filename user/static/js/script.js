document.addEventListener('DOMContentLoaded', function () {
    var calendarEl = document.getElementById('calendar');
    var calendar = new FullCalendar.Calendar(calendarEl, {
        initialView: 'dayGridMonth',
        locale: 'pt-br',
        selectable: true,
        dateClick: function (info) {
            // Redireciona para a página de cadastro com a data selecionada como parâmetro
            window.location.href = `/cadastro/?data=${info.dateStr}`;
        }
    });
    calendar.render();
});