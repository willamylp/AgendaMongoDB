function loading(opcao) {
    if (opcao == 'login') {
        setTimeout(function () {
            window.location.href = "../principal";
        }, 500);
    }
    else {
        setTimeout(function () {
            window.location.href = "../logout";
        }, 500);
    }
}