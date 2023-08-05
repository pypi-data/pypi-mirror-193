//
// This file auto-generated with generate-wrappers.js
//
// Load all three.js python wrappers
var loadedModules = [
    require('./BaseBufferGeometry.autogen.js'),
    require('./BaseGeometry.autogen.js'),
    require('./BufferAttribute.autogen.js'),
    require('./BufferAttribute.js'),
    require('./BufferGeometry.autogen.js'),
    require('./BufferGeometry.js'),
    require('./Clock.autogen.js'),
    require('./DirectGeometry.autogen.js'),
    require('./EventDispatcher.autogen.js'),
    require('./Geometry.autogen.js'),
    require('./Geometry.js'),
    require('./InstancedBufferAttribute.autogen.js'),
    require('./InstancedBufferGeometry.autogen.js'),
    require('./InstancedBufferGeometry.js'),
    require('./InstancedInterleavedBuffer.autogen.js'),
    require('./InstancedInterleavedBuffer.js'),
    require('./InterleavedBuffer.autogen.js'),
    require('./InterleavedBuffer.js'),
    require('./InterleavedBufferAttribute.autogen.js'),
    require('./Layers.autogen.js'),
    require('./Object3D.autogen.js'),
    require('./Object3D.js'),
    require('./Raycaster.autogen.js'),
    require('./Renderer.js'),
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

