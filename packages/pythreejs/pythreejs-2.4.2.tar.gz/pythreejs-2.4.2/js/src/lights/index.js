//
// This file auto-generated with generate-wrappers.js
//
// Load all three.js python wrappers
var loadedModules = [
    require('./AmbientLight.autogen.js'),
    require('./DirectionalLight.autogen.js'),
    require('./DirectionalLightShadow.autogen.js'),
    require('./HemisphereLight.autogen.js'),
    require('./Light.autogen.js'),
    require('./LightShadow.autogen.js'),
    require('./LightShadow.js'),
    require('./PointLight.autogen.js'),
    require('./RectAreaLight.autogen.js'),
    require('./SpotLight.autogen.js'),
    require('./SpotLightShadow.autogen.js'),
];

for (var i in loadedModules) {
    if (Object.prototype.hasOwnProperty.call(loadedModules, i)) {
        var loadedModule = loadedModules[i];
        for (var target_name in loadedModule) {
            if (Object.prototype.hasOwnProperty.call(loadedModule, target_name)) {
                module.exports[target_name] = loadedModule[target_name];
            }
        }
    }
}

