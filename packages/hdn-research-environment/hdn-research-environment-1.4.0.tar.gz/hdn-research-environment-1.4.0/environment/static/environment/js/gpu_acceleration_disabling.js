$(function() {
    const gpuAccelerationToggle = $('label[for=id_gpu_accelerated], input#id_gpu_accelerated')

    $("input[value=jupyter], input[value=rstudio]").on("change", function() {
        if ($("input[value=jupyter]").is(":checked")) {
            gpuAccelerationToggle.show();
        } else {
            gpuAccelerationToggle.hide();
        }
    });
});