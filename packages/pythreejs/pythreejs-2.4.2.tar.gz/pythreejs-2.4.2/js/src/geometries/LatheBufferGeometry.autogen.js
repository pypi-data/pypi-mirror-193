//
// This file auto-generated with generate-wrappers.js
//

var _ = require('underscore');
var Promise = require('bluebird');
var THREE = require('three');
var widgets = require('@jupyter-widgets/base');
var dataserializers = require('jupyter-dataserializers');
var serializers = require('../_base/serializers');

var BaseBufferGeometryModel = require('../core/BaseBufferGeometry.autogen.js').BaseBufferGeometryModel;


class LatheBufferGeometryModel extends BaseBufferGeometryModel {

    defaults() {
        return _.extend(BaseBufferGeometryModel.prototype.defaults.call(this), {

            points: [],
            segments: 12,
            phiStart: 0,
            phiLength: 6.283185307179586,
            type: "LatheBufferGeometry",

        });
    }

    constructThreeObject() {

        var result = new THREE.LatheBufferGeometry(
            this.convertVectorArrayModelToThree(this.get('points'), 'points'),
            this.get('segments'),
            this.convertFloatModelToThree(this.get('phiStart'), 'phiStart'),
            this.convertFloatModelToThree(this.get('phiLength'), 'phiLength')
        );
        return Promise.resolve(result);

    }

    createPropertiesArrays() {

        BaseBufferGeometryModel.prototype.createPropertiesArrays.call(this);

        this.props_created_by_three['type'] = true;

        this.property_converters['points'] = 'convertVectorArray';
        this.property_converters['segments'] = null;
        this.property_converters['phiStart'] = 'convertFloat';
        this.property_converters['phiLength'] = 'convertFloat';
        this.property_converters['type'] = null;

        this.property_assigners['points'] = 'assignArray';

    }
}

LatheBufferGeometryModel.model_name = 'LatheBufferGeometryModel';
LatheBufferGeometryModel.serializers = {
    ...BaseBufferGeometryModel.serializers,
};

module.exports = {
    LatheBufferGeometryModel: LatheBufferGeometryModel,
};
