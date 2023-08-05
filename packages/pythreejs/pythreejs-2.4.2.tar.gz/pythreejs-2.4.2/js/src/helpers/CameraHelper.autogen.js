//
// This file auto-generated with generate-wrappers.js
//

var _ = require('underscore');
var Promise = require('bluebird');
var THREE = require('three');
var widgets = require('@jupyter-widgets/base');
var dataserializers = require('jupyter-dataserializers');
var serializers = require('../_base/serializers');

var Object3DModel = require('../core/Object3D.js').Object3DModel;

var CameraModel = require('../cameras/Camera.autogen.js').CameraModel;

class CameraHelperModel extends Object3DModel {

    defaults() {
        return _.extend(Object3DModel.prototype.defaults.call(this), {

            camera: null,
            type: "CameraHelper",

        });
    }

    constructThreeObject() {

        var result = new THREE.CameraHelper(
            this.convertThreeTypeModelToThree(this.get('camera'), 'camera')
        );
        return Promise.resolve(result);

    }

    createPropertiesArrays() {

        Object3DModel.prototype.createPropertiesArrays.call(this);
        this.three_properties.push('camera');

        this.props_created_by_three['matrixAutoUpdate'] = true;
        this.props_created_by_three['type'] = true;
        this.props_created_by_three['matrixWorldNeedsUpdate'] = true;

        this.property_converters['camera'] = 'convertThreeType';
        this.property_converters['type'] = null;


    }
}

CameraHelperModel.model_name = 'CameraHelperModel';
CameraHelperModel.serializers = {
    ...Object3DModel.serializers,
    camera: { deserialize: serializers.unpackThreeModel },
};

module.exports = {
    CameraHelperModel: CameraHelperModel,
};
