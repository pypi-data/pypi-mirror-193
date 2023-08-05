//
// This file auto-generated with generate-wrappers.js
//

var _ = require('underscore');
var Promise = require('bluebird');
var THREE = require('three');
var widgets = require('@jupyter-widgets/base');
var dataserializers = require('jupyter-dataserializers');
var serializers = require('../_base/serializers');

var BaseGeometryModel = require('../core/BaseGeometry.autogen.js').BaseGeometryModel;


class ExtrudeGeometryModel extends BaseGeometryModel {

    defaults() {
        return _.extend(BaseGeometryModel.prototype.defaults.call(this), {

            type: "ExtrudeGeometry",

        });
    }

    constructThreeObject() {

        var result = new THREE.ExtrudeGeometry();
        return Promise.resolve(result);

    }

    createPropertiesArrays() {

        BaseGeometryModel.prototype.createPropertiesArrays.call(this);

        this.props_created_by_three['type'] = true;

        this.property_converters['type'] = null;


    }
}

ExtrudeGeometryModel.model_name = 'ExtrudeGeometryModel';
ExtrudeGeometryModel.serializers = {
    ...BaseGeometryModel.serializers,
};

module.exports = {
    ExtrudeGeometryModel: ExtrudeGeometryModel,
};
