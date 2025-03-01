// static/js/main.js

// Enable Bootstrap tooltips
document.addEventListener('DOMContentLoaded', function() {
    var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'))
    var tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
        return new bootstrap.Tooltip(tooltipTriggerEl)
    });
    
    // Auto-dismiss alerts after 5 seconds
    setTimeout(function() {
        var alerts = document.querySelectorAll('.alert');
        alerts.forEach(function(alert) {
            var bsAlert = new bootstrap.Alert(alert);
            bsAlert.close();
        });
    }, 5000);
    
    // Quantity input handlers for product detail
    var quantityInput = document.getElementById('quantity');
    if (quantityInput) {
        var minusBtn = document.getElementById('quantity-minus');
        var plusBtn = document.getElementById('quantity-plus');
        
        minusBtn.addEventListener('click', function() {
            var value = parseInt(quantityInput.value);
            if (value > 1) {
                quantityInput.value = value - 1;
            }
        });
        
        plusBtn.addEventListener('click', function() {
            var value = parseInt(quantityInput.value);
            quantityInput.value = value + 1;
        });
    }
});