//
// This file auto-generated with generate-wrappers.js
//

var _ = require('underscore');
var Promise = require('bluebird');
var THREE = require('three');
var widgets = require('@jupyter-widgets/base');
var dataserializers = require('jupyter-dataserializers');
var serializers = require('../_base/serializers');

var BufferGeometryModel = require('./BufferGeometry.js').BufferGeometryModel;


class InstancedBufferGeometryModel extends BufferGeometryModel {

    defaults() {
        return _.extend(BufferGeometryModel.prototype.defaults.call(this), {

            maxInstancedCount: null,
            type: "InstancedBufferGeometry",

        });
    }

    constructThreeObject() {

        var result = new THREE.InstancedBufferGeometry();
        return Promise.resolve(result);

    }

    createPropertiesArrays() {

        BufferGeometryModel.prototype.createPropertiesArrays.call(this);

        this.props_created_by_three['type'] = true;

        this.property_converters['maxInstancedCount'] = null;
        this.property_converters['type'] = null;


    }
}

InstancedBufferGeometryModel.model_name = 'InstancedBufferGeometryModel';
InstancedBufferGeometryModel.serializers = {
    ...BufferGeometryModel.serializers,
};

module.exports = {
    InstancedBufferGeometryModel: InstancedBufferGeometryModel,
};
