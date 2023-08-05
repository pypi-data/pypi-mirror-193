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


class BaseGeometryModel extends ThreeModel {

    defaults() {
        return _.extend(ThreeModel.prototype.defaults.call(this), {

            name: "",
            type: "BaseGeometry",

        });
    }

    constructThreeObject() {

        var result = new THREE.BaseGeometry();
        return Promise.resolve(result);

    }

    createPropertiesArrays() {

        ThreeModel.prototype.createPropertiesArrays.call(this);

        this.props_created_by_three['type'] = true;

        this.property_converters['name'] = null;
        this.property_converters['type'] = null;


    }
}

BaseGeometryModel.model_name = 'BaseGeometryModel';
BaseGeometryModel.serializers = {
    ...ThreeModel.serializers,
};

module.exports = {
    BaseGeometryModel: BaseGeometryModel,
};
