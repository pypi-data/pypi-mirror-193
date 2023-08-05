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


class AxesHelperModel extends Object3DModel {

    defaults() {
        return _.extend(Object3DModel.prototype.defaults.call(this), {

            size: 1,
            type: "AxesHelper",

        });
    }

    constructThreeObject() {

        var result = new THREE.AxesHelper(
            this.convertFloatModelToThree(this.get('size'), 'size')
        );
        return Promise.resolve(result);

    }

    createPropertiesArrays() {

        Object3DModel.prototype.createPropertiesArrays.call(this);

        this.props_created_by_three['type'] = true;
        this.props_created_by_three['matrixWorldNeedsUpdate'] = true;

        this.property_converters['size'] = 'convertFloat';
        this.property_converters['type'] = null;


    }
}

AxesHelperModel.model_name = 'AxesHelperModel';
AxesHelperModel.serializers = {
    ...Object3DModel.serializers,
};

module.exports = {
    AxesHelperModel: AxesHelperModel,
};
