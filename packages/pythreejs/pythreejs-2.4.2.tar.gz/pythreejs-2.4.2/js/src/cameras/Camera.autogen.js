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


class CameraModel extends Object3DModel {

    defaults() {
        return _.extend(Object3DModel.prototype.defaults.call(this), {

            matrixWorldInverse: [1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,1],
            projectionMatrix: [1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,1],
            type: "Camera",

        });
    }

    constructThreeObject() {

        var result = new THREE.Camera();
        return Promise.resolve(result);

    }

    createPropertiesArrays() {

        Object3DModel.prototype.createPropertiesArrays.call(this);

        this.props_created_by_three['matrixWorldInverse'] = true;
        this.props_created_by_three['projectionMatrix'] = true;
        this.props_created_by_three['type'] = true;
        this.props_created_by_three['matrixWorldNeedsUpdate'] = true;

        this.property_converters['matrixWorldInverse'] = 'convertMatrix';
        this.property_converters['projectionMatrix'] = 'convertMatrix';
        this.property_converters['type'] = null;

        this.property_assigners['matrixWorldInverse'] = 'assignMatrix';
        this.property_assigners['projectionMatrix'] = 'assignMatrix';

    }
}

CameraModel.model_name = 'CameraModel';
CameraModel.serializers = {
    ...Object3DModel.serializers,
};

module.exports = {
    CameraModel: CameraModel,
};
