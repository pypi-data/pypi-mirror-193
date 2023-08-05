//
// This file auto-generated with generate-wrappers.js
//

var _ = require('underscore');
var Promise = require('bluebird');
var THREE = require('three');
var widgets = require('@jupyter-widgets/base');
var dataserializers = require('jupyter-dataserializers');
var serializers = require('../_base/serializers');

var PerspectiveCameraModel = require('./PerspectiveCamera.js').PerspectiveCameraModel;


class ArrayCameraModel extends PerspectiveCameraModel {

    defaults() {
        return _.extend(PerspectiveCameraModel.prototype.defaults.call(this), {

            type: "ArrayCamera",

        });
    }

    constructThreeObject() {

        var result = new THREE.ArrayCamera(
            this.convertFloatModelToThree(this.get('fov'), 'fov'),
            this.convertFloatModelToThree(this.get('aspect'), 'aspect'),
            this.convertFloatModelToThree(this.get('near'), 'near'),
            this.convertFloatModelToThree(this.get('far'), 'far')
        );
        return Promise.resolve(result);

    }

    createPropertiesArrays() {

        PerspectiveCameraModel.prototype.createPropertiesArrays.call(this);

        this.props_created_by_three['matrixWorldInverse'] = true;
        this.props_created_by_three['projectionMatrix'] = true;
        this.props_created_by_three['type'] = true;
        this.props_created_by_three['matrixWorldNeedsUpdate'] = true;

        this.property_converters['type'] = null;


    }
}

ArrayCameraModel.model_name = 'ArrayCameraModel';
ArrayCameraModel.serializers = {
    ...PerspectiveCameraModel.serializers,
};

module.exports = {
    ArrayCameraModel: ArrayCameraModel,
};
