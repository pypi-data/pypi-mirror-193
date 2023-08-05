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


class ParametricGeometryModel extends BaseGeometryModel {

    defaults() {
        return _.extend(BaseGeometryModel.prototype.defaults.call(this), {

            func: function(u, v, vec) { },
            slices: 3,
            stacks: 3,
            type: "ParametricGeometry",

        });
    }

    constructThreeObject() {

        var result = new THREE.ParametricGeometry(
            this.convertFunctionModelToThree(this.get('func'), 'func'),
            this.get('slices'),
            this.get('stacks')
        );
        return Promise.resolve(result);

    }

    createPropertiesArrays() {

        BaseGeometryModel.prototype.createPropertiesArrays.call(this);

        this.props_created_by_three['type'] = true;

        this.property_converters['func'] = 'convertFunction';
        this.property_converters['slices'] = null;
        this.property_converters['stacks'] = null;
        this.property_converters['type'] = null;


    }
}

ParametricGeometryModel.model_name = 'ParametricGeometryModel';
ParametricGeometryModel.serializers = {
    ...BaseGeometryModel.serializers,
};

module.exports = {
    ParametricGeometryModel: ParametricGeometryModel,
};
