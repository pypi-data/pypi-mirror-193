//
// This file auto-generated with generate-wrappers.js
//

var _ = require('underscore');
var Promise = require('bluebird');
var THREE = require('three');
var widgets = require('@jupyter-widgets/base');
var dataserializers = require('jupyter-dataserializers');
var serializers = require('../_base/serializers');

var ThreeModel = require('../_base/Three.js').ThreeModel;

var Object3DModel = require('../core/Object3D.js').Object3DModel;

class ControlsModel extends ThreeModel {

    defaults() {
        return _.extend(ThreeModel.prototype.defaults.call(this), {

            controlling: null,

        });
    }

    constructThreeObject() {

        var result = new THREE.Controls();
        return Promise.resolve(result);

    }

    createPropertiesArrays() {

        ThreeModel.prototype.createPropertiesArrays.call(this);
        this.three_properties.push('controlling');


        this.property_converters['controlling'] = 'convertThreeType';


    }
}

ControlsModel.model_name = 'ControlsModel';
ControlsModel.serializers = {
    ...ThreeModel.serializers,
    controlling: { deserialize: serializers.unpackThreeModel },
};

module.exports = {
    ControlsModel: ControlsModel,
};
