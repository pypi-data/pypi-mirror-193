//
// This file auto-generated with generate-wrappers.js
//

var _ = require('underscore');
var Promise = require('bluebird');
var THREE = require('three');
var widgets = require('@jupyter-widgets/base');
var dataserializers = require('jupyter-dataserializers');
var serializers = require('../_base/serializers');

var BufferAttributeModel = require('./BufferAttribute.js').BufferAttributeModel;


class InstancedBufferAttributeModel extends BufferAttributeModel {

    defaults() {
        return _.extend(BufferAttributeModel.prototype.defaults.call(this), {

            meshPerAttribute: 1,

        });
    }

    constructThreeObject() {

        var result = new THREE.InstancedBufferAttribute(
            this.convertArrayBufferModelToThree(this.get('array'), 'array'),
            this.get('meshPerAttribute')
        );
        return Promise.resolve(result);

    }

    createPropertiesArrays() {

        BufferAttributeModel.prototype.createPropertiesArrays.call(this);

        this.props_created_by_three['version'] = true;
        this.props_created_by_three['needsUpdate'] = true;

        this.property_converters['meshPerAttribute'] = null;


    }
}

InstancedBufferAttributeModel.model_name = 'InstancedBufferAttributeModel';
InstancedBufferAttributeModel.serializers = {
    ...BufferAttributeModel.serializers,
};

module.exports = {
    InstancedBufferAttributeModel: InstancedBufferAttributeModel,
};
