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


class CubeCameraModel extends Object3DModel {

    defaults() {
        return _.extend(Object3DModel.prototype.defaults.call(this), {

            type: "CubeCamera",

        });
    }

    constructThreeObject() {

        var result = new THREE.CubeCamera();
        return Promise.resolve(result);

    }

    createPropertiesArrays() {

        Object3DModel.prototype.createPropertiesArrays.call(this);

        this.props_created_by_three['type'] = true;
        this.props_created_by_three['matrixWorldNeedsUpdate'] = true;

        this.property_converters['type'] = null;


    }
}

CubeCameraModel.model_name = 'CubeCameraModel';
CubeCameraModel.serializers = {
    ...Object3DModel.serializers,
};

module.exports = {
    CubeCameraModel: CubeCameraModel,
};
