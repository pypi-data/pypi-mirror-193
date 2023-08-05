//
// This file auto-generated with generate-wrappers.js
//

var _ = require('underscore');
var Promise = require('bluebird');
var THREE = require('three');
var widgets = require('@jupyter-widgets/base');
var dataserializers = require('jupyter-dataserializers');
var serializers = require('../_base/serializers');

var CameraModel = require('./Camera.autogen.js').CameraModel;


class OrthographicCameraModel extends CameraModel {

    defaults() {
        return _.extend(CameraModel.prototype.defaults.call(this), {

            zoom: 1,
            left: 0,
            right: 0,
            top: 0,
            bottom: 0,
            near: 0.1,
            far: 2000,
            type: "OrthographicCamera",

        });
    }

    constructThreeObject() {

        var result = new THREE.OrthographicCamera(
            this.convertFloatModelToThree(this.get('left'), 'left'),
            this.convertFloatModelToThree(this.get('right'), 'right'),
            this.convertFloatModelToThree(this.get('top'), 'top'),
            this.convertFloatModelToThree(this.get('bottom'), 'bottom'),
            this.convertFloatModelToThree(this.get('near'), 'near'),
            this.convertFloatModelToThree(this.get('far'), 'far')
        );
        return Promise.resolve(result);

    }

    createPropertiesArrays() {

        CameraModel.prototype.createPropertiesArrays.call(this);

        this.props_created_by_three['matrixWorldInverse'] = true;
        this.props_created_by_three['projectionMatrix'] = true;
        this.props_created_by_three['type'] = true;
        this.props_created_by_three['matrixWorldNeedsUpdate'] = true;

        this.property_converters['zoom'] = 'convertFloat';
        this.property_converters['left'] = 'convertFloat';
        this.property_converters['right'] = 'convertFloat';
        this.property_converters['top'] = 'convertFloat';
        this.property_converters['bottom'] = 'convertFloat';
        this.property_converters['near'] = 'convertFloat';
        this.property_converters['far'] = 'convertFloat';
        this.property_converters['type'] = null;


    }
}

OrthographicCameraModel.model_name = 'OrthographicCameraModel';
OrthographicCameraModel.serializers = {
    ...CameraModel.serializers,
};

module.exports = {
    OrthographicCameraModel: OrthographicCameraModel,
};
