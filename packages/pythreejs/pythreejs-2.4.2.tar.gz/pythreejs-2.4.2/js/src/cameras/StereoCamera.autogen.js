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

var PerspectiveCameraModel = require('./PerspectiveCamera.js').PerspectiveCameraModel;

class StereoCameraModel extends ThreeModel {

    defaults() {
        return _.extend(ThreeModel.prototype.defaults.call(this), {

            aspect: 1,
            eyeSep: 0.064,
            cameraL: null,
            cameraR: null,

        });
    }

    constructThreeObject() {

        var result = new THREE.StereoCamera();
        return Promise.resolve(result);

    }

    createPropertiesArrays() {

        ThreeModel.prototype.createPropertiesArrays.call(this);
        this.three_properties.push('cameraL');
        this.three_properties.push('cameraR');


        this.property_converters['aspect'] = 'convertFloat';
        this.property_converters['eyeSep'] = 'convertFloat';
        this.property_converters['cameraL'] = 'convertThreeType';
        this.property_converters['cameraR'] = 'convertThreeType';


    }
}

StereoCameraModel.model_name = 'StereoCameraModel';
StereoCameraModel.serializers = {
    ...ThreeModel.serializers,
    cameraL: { deserialize: serializers.unpackThreeModel },
    cameraR: { deserialize: serializers.unpackThreeModel },
};

module.exports = {
    StereoCameraModel: StereoCameraModel,
};
