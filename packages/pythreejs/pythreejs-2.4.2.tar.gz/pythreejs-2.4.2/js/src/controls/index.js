//
// This file auto-generated with generate-wrappers.js
//
// Load all three.js python wrappers
var loadedModules = [
    require('./Controls.autogen.js'),
    require('./FlyControls.autogen.js'),
    require('./FlyControls.js'),
    require('./OrbitControls.autogen.js'),
    require('./OrbitControls.js'),
    require('./Picker.autogen.js'),
    require('./Picker.js'),
    require('./TrackballControls.autogen.js'),
    require('./TrackballControls.js'),
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

